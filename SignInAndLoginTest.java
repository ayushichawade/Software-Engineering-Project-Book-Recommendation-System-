import static org.junit.Assert.*;
import org.junit.Test;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class SignInAndLoginTest {
    
    @Test
    public void testSignUpAndLogin() {
        SignInAndLogin.main(new String[]{});
        String simulatedUserInput = "1\nusername\npassword\n2\nusername\npassword\n3\n";
        System.setIn(new ByteArrayInputStream(simulatedUserInput.getBytes()));
        
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));
        
        SignInAndLogin.main(new String[]{});
        String output = outputStream.toString();
        
        assertTrue(output.contains("User registered successfully."));
        assertTrue(output.contains("Login successful. Welcome, username!"));
    }
}
