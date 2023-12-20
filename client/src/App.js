import Login from './pages/Login';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';
import Otp from './pages/Otp';
import Error from './pages/Error';
import Headers from './components/Headers';
import { Routes, Route } from "react-router-dom"
import 'bootstrap/dist/css/bootstrap.min.css';
import 'react-toastify/dist/ReactToastify.css';
import './App.css';
import Page1 from './pages/page1';
import Page2 from './pages/page2';
import Page3 from './paage/page3';
import Page4 from './paage/page4';
import Page5 from './paage/page5';
import Page6 from './paage/page6';
import Page7 from './paage/page7';
import Page8 from './paage/page8';
import Page9 from './paage/page9';
import Page10 from './paage/page10';
import Page11 from './paage/page11';
import Page12 from './paage/page12';
import All from './models/all';
import Dt from './models/dectree';
import Knn from './models/knn';
import Lr from './models/logic';
import Nb from './models/nb';
import Rf from './models/randfor';
import Svm from './models/svm';

function App() {
  return (
    <>
      <Headers />
      <Routes>
      <Route path='/' element={<Login />} />
        <Route path='/register' element={<Register />} />
        <Route path='/dashboard' element={<Dashboard />} />
        <Route path='/dectree' element={<Dt />} />
        <Route path='/randfor' element={<Rf />} />
        <Route path='/logic' element={<Lr />} />
        <Route path='/knn' element={<Knn />} />
        <Route path='/svm' element={<Svm />} />
        <Route path='/nb' element={<Nb />} />
        <Route path='/all' element={<All />} />
        <Route path='/user/otp' element={<Otp />} />
        <Route path="/api" element={<Page1 />} />
        <Route path="/api1" element={<Page2 />} />
        <Route path="/api3" element={<Page3 />} />
        <Route path="/api4" element={<Page4 />} />
        <Route path="/api5" element={<Page5 />} />
        <Route path="/api6" element={<Page6 />} />
        <Route path="/api7" element={<Page7 />} />
        <Route path="/api8" element={<Page8 />} />
        <Route path="/api9" element={<Page9 />} />
        <Route path="/api10" element={<Page10 />} />
        <Route path="/api11" element={<Page11/>} />
        <Route path="/api12" element={<Page12/>} />
        <Route path='*' element={<Error />} />

      </Routes>
    </>
  );
}

export default App;
