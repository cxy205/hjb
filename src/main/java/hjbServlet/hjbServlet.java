package hjbServlet;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet(urlPatterns = "/")
public class hjbServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("---执行了doPost---");
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("---执行了doGet---");
    }

    protected void processData(javax.servlet.http.HttpServletRequest request, javax.servlet.http.HttpServletResponse response) throws javax.servlet.ServletException, IOException {
        System.out.println("---处理数据---");
        response.setContentType("text/xml;charset=utf-8");
        response.setCharacterEncoding("utf-8");
        response.setHeader("Cache-Control","no-cache");
        //String deviceId=request.getParameter("device_id");
        String test="test";
        response.setContentType("text/html; charset=UTF-8");
        try{
            response.getWriter().print(test);
            response.getWriter().flush();
            response.getWriter().close();
        } catch(IOException e){
            e.printStackTrace();
        }
    }

    protected void service(javax.servlet.http.HttpServletRequest request, javax.servlet.http.HttpServletResponse response) throws javax.servlet.ServletException, IOException {
        System.out.println("---执行了service---");
        processData(request,response);
    }
}
