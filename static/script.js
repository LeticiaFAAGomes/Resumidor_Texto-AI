document.getElementById("botaoResumo").addEventListener("click", resumirTexto);

async function resumirTexto() {
  const usuario = document.getElementById("usuario").value;
  const resposta = await fetch("/summarize", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text: usuario }),
  });
  const data = await resposta.json();
  document.getElementById("resumo").innerText = data.summary;
}
