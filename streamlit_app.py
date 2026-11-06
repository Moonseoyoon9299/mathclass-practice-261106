import streamlit as st
from textwrap import dedent

st.set_page_config(
    page_title='나를 소개합니다',
    page_icon='✨',
    layout='wide',
    initial_sidebar_state='collapsed',
)

st.html(
    dedent("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    :root {
        --ink: #17211d;
        --paper: #f7f8f2;
        --coral: #ff6257;
        --orange: #ff9638;
        --yellow: #ffd447;
        --lime: #b7df50;
        --green: #39b879;
        --mint: #73d6b1;
        --teal: #27b8b2;
        --cyan: #62c9e8;
        --blue: #4285ef;
        --indigo: #5c61d8;
        --violet: #9c78e8;
        --pink: #f47eae;
        --rose: #ed527d;
        --white: #fffefa;
    }

    [data-testid="stAppViewContainer"] {
        background-color: var(--paper);
        background-image: radial-gradient(#17211d12 0.7px, transparent 0.7px);
        background-size: 15px 15px;
    }
    [data-testid="stHeader"] { background: transparent; }
    .block-container {
        max-width: 1200px;
        padding: 1rem 2.2rem 5rem;
    }
    .portfolio {
        color: var(--ink);
        font-family: 'Gowun Dodum', sans-serif;
    }
    .rainbow {
        display: grid;
        grid-template-columns: repeat(14, 1fr);
        height: 9px;
        overflow: hidden;
        border-radius: 2px;
    }
    .rainbow span:nth-child(14n + 1) { background: var(--coral); }
    .rainbow span:nth-child(14n + 2) { background: var(--orange); }
    .rainbow span:nth-child(14n + 3) { background: var(--yellow); }
    .rainbow span:nth-child(14n + 4) { background: var(--lime); }
    .rainbow span:nth-child(14n + 5) { background: var(--green); }
    .rainbow span:nth-child(14n + 6) { background: var(--mint); }
    .rainbow span:nth-child(14n + 7) { background: var(--teal); }
    .rainbow span:nth-child(14n + 8) { background: var(--cyan); }
    .rainbow span:nth-child(14n + 9) { background: var(--blue); }
    .rainbow span:nth-child(14n + 10) { background: var(--indigo); }
    .rainbow span:nth-child(14n + 11) { background: var(--violet); }
    .rainbow span:nth-child(14n + 12) { background: var(--pink); }
    .rainbow span:nth-child(14n + 13) { background: var(--rose); }
    .rainbow span:nth-child(14n) { background: var(--coral); }
    .topline {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 18px 0 24px;
        border-bottom: 1px solid #17211d35;
        font-size: 13px;
        letter-spacing: 0;
    }
    .topline strong { font-family: 'Space Grotesk', sans-serif; font-size: 15px; }
    .topline a { color: var(--ink); text-decoration: none; margin-left: 22px; }
    .hero {
        display: grid;
        grid-template-columns: 1.05fr 0.95fr;
        gap: 7%;
        align-items: center;
        padding: 74px 0 84px;
    }
    .eyebrow, .section-kicker {
        margin: 0 0 18px;
        color: #53615a;
        font-family: 'Space Grotesk', 'Gowun Dodum', sans-serif;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0;
        text-transform: uppercase;
    }
    .eyebrow span {
        display: inline-block;
        width: 10px;
        height: 10px;
        margin-right: 8px;
        border-radius: 50%;
        background: var(--coral);
    }
    .hero h1 {
        margin: 0;
        font-size: clamp(42px, 6vw, 76px);
        line-height: 1.18;
        font-weight: 400;
        letter-spacing: 0;
    }
    .hero h1 .name {
        display: inline-block;
        padding: 0 8px 4px;
        background: var(--yellow);
        font-weight: 700;
    }
    .spark { color: var(--rose); font-size: 0.58em; vertical-align: top; }
    .hero-copy { max-width: 530px; }
    .hero-intro { max-width: 430px; margin: 24px 0 25px; color: #53615a; font-size: 17px; line-height: 1.9; }
    .hero-link {
        display: inline-block;
        padding: 12px 18px;
        border: 1px solid var(--ink);
        border-radius: 2px;
        color: var(--ink);
        font-size: 14px;
        text-decoration: none;
        transition: background 160ms ease, color 160ms ease;
    }
    .hero-link:hover { background: var(--ink); color: var(--white); }
    .hero-art { position: relative; min-height: 390px; padding: 0 20px 20px 0; }
    .hero-art::before {
        position: absolute;
        z-index: 0;
        top: 22px;
        right: 0;
        bottom: 0;
        left: 22px;
        background: var(--teal);
        content: '';
    }
    .hero-art img {
        position: relative;
        z-index: 1;
        width: 100%;
        height: 390px;
        border-radius: 2px;
        object-fit: cover;
        object-position: center 38%;
        filter: saturate(1.08);
    }
    .photo-note {
        position: absolute;
        z-index: 2;
        right: -9px;
        bottom: 5px;
        padding: 11px 15px;
        transform: rotate(-3deg);
        background: var(--yellow);
        font-size: 12px;
    }
    .section { padding: 72px 0; border-top: 1px solid #17211d35; }
    .section-heading { display: flex; justify-content: space-between; align-items: end; gap: 20px; margin-bottom: 32px; }
    .section-heading h2 { margin: 0; font-size: 38px; line-height: 1.25; font-weight: 400; }
    .section-number { color: #738078; font-family: 'Space Grotesk', sans-serif; font-size: 13px; }
    .about-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0; border-top: 1px solid #17211d35; }
    .about-item { min-height: 178px; padding: 24px 23px 15px 0; border-right: 1px solid #17211d35; }
    .about-item + .about-item { padding-left: 23px; }
    .about-item:last-child { border-right: 0; }
    .label { display: block; margin-bottom: 20px; color: #53615a; font-size: 13px; }
    .about-item strong { display: block; font-size: 22px; font-weight: 400; line-height: 1.55; }
    .about-item p { margin: 10px 0 0; color: #657169; font-size: 14px; line-height: 1.8; }
    .dream {
        display: grid;
        grid-template-columns: 0.72fr 1.28fr;
        gap: 30px;
        align-items: center;
        margin-top: 38px;
        padding: 34px 38px;
        background: var(--indigo);
        color: white;
    }
    .dream .section-kicker { color: #e2e3ff; }
    .dream blockquote { margin: 0; font-size: 25px; line-height: 1.7; }
    .dream mark { padding: 0 5px; background: var(--yellow); color: var(--ink); }
    .trip-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }
    .trip { min-width: 0; }
    .trip img { display: block; width: 100%; height: 220px; border-radius: 2px; object-fit: cover; }
    .trip:nth-child(1) img { border-bottom: 7px solid var(--orange); }
    .trip:nth-child(2) img { border-bottom: 7px solid var(--pink); }
    .trip:nth-child(3) img { border-bottom: 7px solid var(--blue); }
    .trip-meta { display: flex; justify-content: space-between; gap: 10px; align-items: baseline; padding-top: 13px; }
    .trip-meta strong { font-size: 20px; font-weight: 400; }
    .trip-meta span { color: #657169; font-size: 12px; }
    .hometown {
        display: grid;
        grid-template-columns: 1fr 1fr;
        min-height: 270px;
        background: var(--coral);
    }
    .hometown-copy { align-self: center; padding: 36px 42px; }
    .hometown-copy .section-kicker { color: #51251f; }
    .hometown h3 { margin: 0 0 14px; font-size: 42px; font-weight: 400; }
    .hometown p { max-width: 390px; margin: 0; line-height: 1.9; }
    .hometown-art {
        display: grid;
        place-items: center;
        min-height: 270px;
        background: var(--cyan);
        color: var(--ink);
        font-family: 'Space Grotesk', sans-serif;
        font-size: 76px;
        font-weight: 700;
    }
    .hobby-list { display: flex; flex-wrap: wrap; gap: 12px; margin: 0; padding: 0; list-style: none; }
    .hobby-list li { padding: 12px 17px; border: 1px solid var(--ink); border-radius: 2px; font-size: 15px; }
    .hobby-list li:nth-child(6n + 1) { background: var(--lime); }
    .hobby-list li:nth-child(6n + 2) { background: var(--pink); }
    .hobby-list li:nth-child(6n + 3) { background: var(--yellow); }
    .hobby-list li:nth-child(6n + 4) { background: var(--mint); }
    .hobby-list li:nth-child(6n + 5) { background: var(--violet); }
    .hobby-list li:nth-child(6n) { background: var(--orange); }
    .dog {
        display: grid;
        grid-template-columns: 0.9fr 1.1fr;
        align-items: center;
        gap: 7%;
        padding: 28px 0 15px;
    }
    .dog img { width: 100%; height: 300px; border-radius: 2px; object-fit: cover; }
    .dog h3 { margin: 0 0 12px; font-size: 40px; font-weight: 400; }
    .dog h3 span { padding: 0 6px; background: var(--yellow); }
    .dog p { max-width: 420px; color: #53615a; font-size: 15px; line-height: 1.9; }
    .dog-stamp { display: inline-block; margin-top: 10px; padding: 8px 12px; transform: rotate(-2deg); background: var(--rose); color: white; font-family: 'Space Grotesk', sans-serif; font-size: 12px; }
    .footer { display: flex; justify-content: space-between; gap: 15px; padding: 22px 0 0; border-top: 1px solid #17211d35; color: #657169; font-size: 12px; }

    @media (max-width: 760px) {
        .block-container { padding: 0.6rem 1.1rem 3rem; }
        .topline { align-items: flex-start; }
        .topline nav { display: flex; flex-wrap: wrap; justify-content: flex-end; gap: 9px 14px; max-width: 220px; }
        .topline a { margin-left: 0; }
        .hero { grid-template-columns: 1fr; gap: 34px; padding: 48px 0 58px; }
        .hero h1 { font-size: 48px; }
        .hero-art, .hero-art img { min-height: 300px; height: 300px; }
        .section { padding: 52px 0; }
        .section-heading h2 { font-size: 31px; }
        .about-grid { grid-template-columns: 1fr; }
        .about-item, .about-item + .about-item { min-height: auto; padding: 19px 0; border-right: 0; border-bottom: 1px solid #17211d35; }
        .about-item:last-child { border-bottom: 0; }
        .label { margin-bottom: 7px; }
        .dream { grid-template-columns: 1fr; gap: 5px; margin-top: 26px; padding: 26px 23px; }
        .dream blockquote { font-size: 20px; }
        .trip-grid { grid-template-columns: 1fr; gap: 25px; }
        .trip img { height: 230px; }
        .hometown { grid-template-columns: 1fr; }
        .hometown-copy { padding: 28px 24px; }
        .hometown-art { min-height: 185px; font-size: 60px; }
        .dog { grid-template-columns: 1fr; gap: 24px; }
        .dog img { height: 240px; }
        .dog h3 { font-size: 34px; }
        .footer { flex-direction: column; }
    }
    </style>
    """),
)

st.html(
    dedent("""
    <main class="portfolio">
        <div class="rainbow"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>
        <header class="topline">
            <strong>MY LITTLE UNIVERSE ✳</strong>
            <nav aria-label="페이지 메뉴">
                <a href="#about">소개</a><a href="#travel">여행</a><a href="#hobbies">취미</a><a href="#buddy">우리집 강아지</a>
            </nav>
        </header>

        <section class="hero">
            <div class="hero-copy">
                <p class="eyebrow"><span></span> NICE TO MEET YOU · 2026</p>
                <h1>안녕하세요,<br><span class="name">문서윤</span>입니다<span class="spark"> ✳</span></h1>
                <p class="hero-intro">좋아하는 것들을 하나씩 모아 만든 나의 작은 소개 페이지예요. 새로운 사람과 장소를 만나며 매일 조금씩 자라고 있어요.</p>
                <a class="hero-link" href="#about">나를 더 알아보기 <span aria-hidden="true">↘</span></a>
            </div>
            <div class="hero-art">
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=1100&q=85" alt="프로필 사진 자리">
                <span class="photo-note">여기에 내 사진을 넣어주세요!</span>
            </div>
        </section>

        <section class="section" id="about">
            <div class="section-heading">
                <div><p class="section-kicker">A FEW THINGS ABOUT ME</p><h2>나를 소개할게요</h2></div>
                <span class="section-number">01 / ABOUT</span>
            </div>
            <div class="about-grid">
                <div class="about-item"><span class="label">내 소개</span><strong>미래의 교사<br>배움의 즐거움을 나누고 싶어요.</strong><p>사람들과 함께 배우며 성장하는 것을 좋아해요.</p></div>
                <div class="about-item"><span class="label">나의 소속</span><strong>청주교육대학교<br>사회과교육과</strong><p>사회과교육을 공부하고 있어요.</p></div>
                <div class="about-item"><span class="label">요즘 관심사</span><strong>배우고 가르치며,<br>함께 성장하기</strong><p>좋은 선생님이 되기 위해 한 걸음씩 배우는 중이에요.</p></div>
            </div>
            <div class="dream">
                <p class="section-kicker">BIG DREAMS</p>
                <blockquote>나의 꿈은 <mark>교사</mark>가 되어<br>배움의 즐거움을 나누는 사람이 되는 거예요.</blockquote>
            </div>
        </section>

        <section class="section" id="travel">
            <div class="section-heading">
                <div><p class="section-kicker">POSTCARDS FROM MY TRIPS</p><h2>여행의 기억</h2></div>
                <span class="section-number">02 / PLACES</span>
            </div>
            <div class="trip-grid">
                <article class="trip"><img src="https://images.unsplash.com/photo-1570789210967-2cac24afeb00?auto=format&fit=crop&w=900&q=85" alt="제주도 여행 사진"><div class="trip-meta"><strong>제주도</strong><span>바다가 좋았던 여행</span></div></article>
                <article class="trip"><img src="https://images.unsplash.com/photo-1555881400-74d7acaacd8b?auto=format&fit=crop&w=900&q=85" alt="부산 여행 사진"><div class="trip-meta"><strong>부산</strong><span>다시 가고 싶은 곳</span></div></article>
                <article class="trip"><img src="https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=900&q=85" alt="일본 여행 사진"><div class="trip-meta"><strong>일본</strong><span>기억에 남는 여행</span></div></article>
            </div>
        </section>

        <section class="section">
            <div class="section-heading">
                <div><p class="section-kicker">WHERE I COME FROM</p><h2>나의 고향</h2></div>
                <span class="section-number">03 / HOME</span>
            </div>
            <div class="hometown">
                <div class="hometown-copy"><p class="section-kicker">MY HOMETOWN</p><h3>제천, 나의 고향</h3><p>익숙한 풍경과 추억이 있는 제천. 고향에서 좋아하는 장소와 이야기를 소개해요.</p></div>
                <div class="hometown-art" aria-label="나의 고향을 상징하는 글자">HOME ↗</div>
            </div>
        </section>

        <section class="section" id="hobbies">
            <div class="section-heading">
                <div><p class="section-kicker">LITTLE THINGS I LOVE</p><h2>내가 좋아하는 것</h2></div>
                <span class="section-number">04 / HOBBIES</span>
            </div>
            <ul class="hobby-list">
                <li>사진 찍기</li><li>여행 계획하기</li><li>음악 듣기</li><li>맛있는 것 먹기</li><li>책 읽기</li><li>산책하기</li>
            </ul>
        </section>

        <section class="section" id="buddy">
            <div class="section-heading">
                <div><p class="section-kicker">MY FAVORITE ROOMMATE</p><h2>우리집 귀염둥이</h2></div>
                <span class="section-number">05 / BEST FRIEND</span>
            </div>
            <div class="dog">
                <img src="https://images.unsplash.com/photo-1552053831-71594a27632d?auto=format&fit=crop&w=1000&q=85" alt="강아지 사진 자리">
                <div><p class="section-kicker">A VERY GOOD DOG</p><h3>우리 강아지 <span>초코</span></h3><p>산책과 간식을 세상에서 제일 좋아하는 우리집 막내 초코예요. 함께하는 즐거운 이야기를 소개해요.</p><span class="dog-stamp">BEST BUDDY ♡</span></div>
            </div>
        </section>

        <footer class="footer"><span>이 페이지는 나의 이야기로 채워가는 중 ✳</span><span>MADE WITH A LITTLE BIT OF EVERYTHING</span></footer>
    </main>
    """),
)
