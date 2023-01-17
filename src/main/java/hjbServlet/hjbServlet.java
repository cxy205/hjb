package hjbServlet;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.*;
import java.nio.charset.Charset;

@WebServlet(name="hjbServlet",urlPatterns = "/hjbServlet")
public class hjbServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("---执行了doPost---");
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("---执行了doGet---");

        String msg =request.getParameter("data");
    }


    protected void processData(javax.servlet.http.HttpServletRequest request, javax.servlet.http.HttpServletResponse response) throws javax.servlet.ServletException, IOException {
        System.out.println("---处理数据---");
        String msg =request.getParameter("msg");
        String msg2 = java.net.URLDecoder.decode(msg,"UTF-8");
        System.out.println(msg);
        System.out.println(msg2);
        String test="test";

        try{
            String[] args1=new String[] {"python","C:\\Users\\29693\\Desktop\\hjb-master\\src\\main\\utils\\python\\test_chat.py",msg2};
            Process proc=Runtime.getRuntime().exec(args1);

            BufferedReader in=new BufferedReader(new InputStreamReader(proc.getInputStream(), Charset.forName("GBK")));
            test=in.readLine();
            System.out.println(test);
            in.close();
            int res=proc.waitFor();
            System.out.println(res);
        }catch (IOException e){
            e.printStackTrace();
        }catch (InterruptedException e){
            e.printStackTrace();
        }

        response.setCharacterEncoding("utf-8");
        response.setHeader("Cache-Control","no-cache");
        //String deviceId=request.getParameter("device_id");
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
