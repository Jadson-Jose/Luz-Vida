import fs from 'fs';
import path from 'path';

export default async function handler(req, res) {
  try {
    // Lê o index.html gerado pelo Vite (já dentro da pasta dist)
    const htmlPath = path.join(process.cwd(), 'dist', 'index.html');
    let html = fs.readFileSync(htmlPath, 'utf8');

    const { id } = req.query;
    let title = 'Luz-Vida | Bíblia Católica';
    let description = 'A Palavra de Deus viva e acessível. Leia a Bíblia Católica online.';

    // Se houver um ID de capítulo, busca as informações na API do Render
    if (id) {
      try {
        const apiRes = await fetch(`https://luz-vida.onrender.com/api/chapters/${id}/navigation`);
        if (apiRes.ok) {
          const data = await apiRes.json();
          title = `${data.book_name} ${data.chapter_number} | Luz-Vida`;
          description = `Leia ${data.book_name} ${data.chapter_number} na Bíblia Católica Luz-Vida.`;
        }
      } catch (apiError) {
        console.error("Erro ao buscar API do Render:", apiError);
      }
    }

    // Substitui as meta tags no HTML
    html = html.replace(/<title>.*?<\/title>/, `<title>${title}</title>`);
    html = html.replace(/<meta property="og:title" content=".*?" \/>/, `<meta property="og:title" content="${title}" />`);
    html = html.replace(/<meta property="og:description" content=".*?" \/>/, `<meta property="og:description" content="${description}" />`);

    res.setHeader('Content-Type', 'text/html; charset=utf-8');
    // Cache na borda do Vercel por 5 minutos para não sobrecarregar
    res.setHeader('Cache-Control', 's-maxage=300, stale-while-revalidate');
    
    return res.status(200).send(html);
  } catch (error) {
    console.error("Erro ao ler o index.html:", error);
    return res.status(500).send('Erro interno ao gerar o preview.');
  }
}