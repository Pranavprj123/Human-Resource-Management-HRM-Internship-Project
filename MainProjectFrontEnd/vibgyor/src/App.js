// import logo from './logo.svg';
import './App.css';
import { RouterProvider } from 'react-router-dom';
import Route from './Components/Route';
function App() {
  return (
    <div className="App">
      <RouterProvider router={Route()}/>
    </div>
  );
}

export default App;
