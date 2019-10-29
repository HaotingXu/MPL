program convert_raw
  !!Reading and computing the error rate of quantum key distribution
  !!Code by Haoting Xu
  !!2019/10/26
  !------------------------------
  !input file
  implicit none 
  character(LEN=*),parameter::receive_file = "receiver_raw.bin"
  character(LEN=*),parameter::transmit_file = "transmitter_raw.bin"
  character(LEN=1024) line
  integer n,i,j! n is the amount of keys
  integer,dimension(:,:),allocatable:: receive,transmit
  character(LEN=17) tmp1
  character(LEN=2) tmp2
  character(LEN=1) TMP3
  integer error
  real*8 rate
  open(10,FILE = receive_file)
  n=0
  do
     read(10,*,ERR=100,END=100) line
     n=n+1
  end do
  write(*,*) line
100 close(10)
  write(*,*) "Read ",n, " key samples."
  allocate(receive(2,n),transmit(2,n))
  open(10,FILE = receive_file)
  do i=1,n
     read(10,'(A17,I1,A2,I1,A1)') tmp1,receive(1,i),tmp2,receive(2,i),tmp3
  end do
  close(10)
  error=0
     do i=1,n
           if (receive(1,i) /= receive(2,i)) then
              error = error +1
           end if
     end do
     write(*,*)"Error is ",error
     rate = 100.*error/n
     
  write(*,*) "Error rate is ",rate,"%"
end program convert_raw
  
