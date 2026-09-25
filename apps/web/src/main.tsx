import React from "react";
import { createRoot } from "react-dom/client";

function App() {
  return <main><h1>Cosmetics Hub</h1><p>Scaffold inicial do MVP.</p></main>;
}

createRoot(document.getElementById("root")!).render(<React.StrictMode><App /></React.StrictMode>);
